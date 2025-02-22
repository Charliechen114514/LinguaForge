import typer, loguru, os
from rich.console import Console
from rich.panel import Panel
from typing_extensions import Annotated
from linguaforge.helper import CLICommandHelper 
from linguaforge.translator_cli_interface import \
    SingleFileCLICommandArgPasser, SingleDocumentTranslatorCLI, \
    BatchFileCLICommandArgPasser, MultiDocumentTranslatorCLI
from config_controller.config_template_generator import TemplateConfigFormat
from translation_core.batch_path_maker import BatchFilePathMaker,SingtonFileInfo
from history_manager.history_summon import HistoryManager 

app = typer.Typer()
console = Console()
logger = loguru.logger

def controlling_hook(index: int, all: int, info: SingtonFileInfo):
    console.print(Panel.fit(f"[bold blue]current handling with [bold green]{index} / [bold blue]{all}:\n"\
                  f"[bold yellow]{info.src_path} -> [bold green]{info.dest_path}\n", title=f"{index} / {all}"))

def history_callback(path: str):
    try:
        if os.path.exists(path=path):
            raise FileExistsError("file has been exsited! retry a new one!")
        return path
    except FileExistsError as e:
        raise typer.BadParameter(str(e))    


def process_single_by_arg_passer(passer: SingleFileCLICommandArgPasser, req_ensure: bool):
    cli_trans = SingleDocumentTranslatorCLI()
    cli_trans.register_singledocument_args(passer)  
    if req_ensure:
        console.print(Panel.fit("[bold blue]" + cli_trans.config_info(), title="Config Display"))
        if not typer.confirm("Are you sure this configurations?"):
            raise typer.Exit()
    console.print(Panel.fit("[bold blue]waiting for translations", title="Waitings..."))
    try:
        path = cli_trans.process_translations()
    except Exception as e:
        # TODO: For detailed exception handing
        console.print(Panel.fit(f"[bold red]Document translation has failed: {str(e)}", title="Error occurs"))
        raise typer.Exit()
    console.print(Panel.fit("[bold green]Document translation has been summoned at: " + path, title="Finish and enjoy!"))

def process_batch_by_arg_passer(
        passer: BatchFileCLICommandArgPasser, req_ensure: bool):
    cli_trans = MultiDocumentTranslatorCLI()
    cli_trans.register_batchdocument_args(passer)  
    if req_ensure:
        console.print(Panel.fit("[bold blue]" + cli_trans.config_info(), title="Config Display"))
        if not typer.confirm("Are you sure this configurations?"):
            raise typer.Exit()
    lists = cli_trans.generate_listsinfo()
    console.print(Panel.fit("[bold blue]" + BatchFilePathMaker.display_lists(lists), title="Files transform lists"))
    if req_ensure:
        if not typer.confirm("Are you sure this translation lists?"):
            raise typer.Exit()
    console.print(Panel.fit("[bold blue]waiting for translations", title="Waitings..."))
    cli_trans.process_translations(lists)
    console.print(Panel.fit("[bold green]All documentations summon down!", title="Finishing issues"))
    if not typer.confirm("Are you want to create a history file so that you can roll back the change?"):
        raise typer.Exit()
    
    while 1:
        try:
            path = typer.prompt("Given a history file path to store the result!", type=str)
            path = history_callback(path=path)
            console.print(Panel.fit(f"[bold blue]Hist file will summon at {path}", title="History file"))
            if req_ensure and typer.confirm("Are you sure this configurations?"):
                break  
        except typer.BadParameter:
            console.print(Panel.fit(f"[bold red]Hist file: {path} is path-invalid! try another one!", title="History file"))     
    HistoryManager.write_history_file(path, lists)


@app.command()
def single_doc(
    document_path: Annotated[
        str, typer.Option(help=CLICommandHelper.DOCUMENT_PATH_STR, prompt=CLICommandHelper.DOCUMENT_PATH_PROMPT)],
    dest_lang: Annotated[
        str, typer.Option(help=CLICommandHelper.DEST_LANG_STR, prompt=CLICommandHelper.DEST_LANG_PROMPT)],
    split_colon:  Annotated[
        str, typer.Option(help=CLICommandHelper.COLON_STR, prompt=CLICommandHelper.COLON_PROMPT)],
    dest_path: Annotated[
        str, typer.Option(help=CLICommandHelper.DEST_DOC_SUMMON_PATH)] = "",
    req_ensure: Annotated[bool, typer.Option(help="True when user requires the ensurance")] = True
):
    """
        summon single files by console interatives
    """
    passer = SingleFileCLICommandArgPasser(src_doc_path=document_path,
                                 dest_lang=dest_lang,
                                 split_colon=split_colon, 
                                 dest_doc_path=dest_path)
    process_single_by_arg_passer(passer, req_ensure)

@app.command()
def single_doc_from_config(
   config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)], 
    req_ensure: Annotated[bool, typer.Option(help="True when user requires the ensurance")] = True):
    """
        summon single file translations given the config file
    """
    try:
        passer = TemplateConfigFormat.do_singlefile_parse_config(config_path)
    except Exception as e:
        console.print(Panel.fit(f"[bold red]Document config file reading has failed: {str(e)}", title="Error occurs"))
        raise typer.Exit()
    process_single_by_arg_passer(passer, req_ensure)

@app.command()
def batch_doc_from_config(
   config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)], 
    req_ensure: Annotated[bool, typer.Option(help="True when user requires the ensurance")] = True
):
    """
        summon batch files translations given the config file
    """
    try:
        passer = TemplateConfigFormat.do_batchfile_parse_config(config_path)
    except Exception as e:
        console.print(Panel.fit(f"[bold red]Document config file reading has failed: {str(e)}", title="Error occurs"))
        raise typer.Exit()
    process_batch_by_arg_passer(passer, req_ensure)

@app.command()
def remove_trans(
    config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)], 
    req_ensure: Annotated[bool, typer.Option(help="True when user requires the ensurance")] = True
):
    """
        remove the translation by given a hist file records, summon
        when you summon translation previously if you indicate this
    """
    try:
        res = HistoryManager.review_back(config_path)
    except Exception as e:
        console.print(Panel.fit(f"[bold red]History config file reading has failed: {str(e)}", title="Error occurs")) 
        raise typer.Exit()

    lists_trans = [each.dest_path for each in res]
    displays = "\n".join(lists_trans)
    console.print(Panel.fit(f"[bold blue]this files will be removed:\n{displays}", title="Config Display"))
    if req_ensure:
        if not typer.confirm("Are you sure this removings? See this carefully!"):
            raise typer.Exit()
    for each_file in lists_trans:
        try:
            os.remove(each_file)
        except Exception as e:
            console.print(f"[bold yellow]file: when removing file: {each_file} catches error: {str(e)}\n")
        console.print(f"[bold green]file: {each_file} removes!\n")
    console.print(f"[bold green]All files removes down\n")


@app.command()
def gen_sf_config(
    config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)],
    config_type: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIGTYPE_GEN_STR, prompt=CLICommandHelper.CONFIGTYPE_GEN_PROMPT)]
):
    """
        generate single file translagtion template
    """
    if config_type not in TemplateConfigFormat.supportive_format():
        console.print(Panel.fit(
            f"[bold red]The format you pass {config_type} is not supported!"\
            "see the supportive configs: "
            , title="Error occurs"))
        format_file_list()
    TemplateConfigFormat.generate_file_accord_type(config_type, config_path, TemplateConfigFormat.SINGLE_TYPE)
    
@app.command()
def gen_bd_config(
    config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)],
    config_type: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIGTYPE_GEN_STR, prompt=CLICommandHelper.CONFIGTYPE_GEN_PROMPT)]
):
    """
        generate a batch documentations templates
    """
    if config_type not in TemplateConfigFormat.supportive_format():
        console.print(Panel.fit(
            f"[bold red]The format you pass {config_type} is not supported!"\
            "see the supportive configs: "
            , title="Error occurs"))
        format_file_list()
    TemplateConfigFormat.generate_file_accord_type(config_type, config_path, TemplateConfigFormat.DOC_TREE_TYPE)
    



@app.command()
def langs_list():
    """
        check the default lang's supportive langs list
    """
    console.print(Panel.fit(SingleDocumentTranslatorCLI.def_engine_lang_supports(), title="Support languages"))

@app.command()
def format_file_list():
    """
        see the support format of file configure type
    """
    console.print(Panel.fit(TemplateConfigFormat.display_support_format_string(), title="Support config format file"))

if __name__ == "__main__":
    app()