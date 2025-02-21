import typer
import loguru
from rich.console import Console
from rich.panel import Panel
from typing_extensions import Annotated
from linguaforge.helper import CLICommandHelper 
from linguaforge.translator_cli_interface import \
    SingleFileCLICommandArgPasser, DocumentTranslatorCLI, BatchFileCLICommandArgPasser
from config_controller.config_template_generator import TemplateConfigFormat

app = typer.Typer()
console = Console()
logger = loguru.logger

def process_single_by_arg_passer(passer: SingleFileCLICommandArgPasser, req_ensure: bool):
    cli_trans = DocumentTranslatorCLI()
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

def process_batch_by_arg_passer(passer: BatchFileCLICommandArgPasser, req_ensure: bool):
    cli_trans = DocumentTranslatorCLI()
    cli_trans.register_batchdocument_args(passer)  
    if req_ensure:
        console.print(Panel.fit("[bold blue]" + cli_trans.config_info(), title="Config Display"))
        if not typer.confirm("Are you sure this configurations?"):
            raise typer.Exit()
    # console.print(Panel.fit("[bold blue]waiting for translations", title="Waitings..."))


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
    passer = SingleFileCLICommandArgPasser(src_doc_path=document_path,
                                 dest_lang=dest_lang,
                                 split_colon=split_colon, 
                                 dest_doc_path=dest_path)
    process_single_by_arg_passer(passer, req_ensure)

@app.command()
def single_doc_from_config(
   config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)], 
    req_ensure: Annotated[bool, typer.Option(help="True when user requires the ensurance")] = True
):
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
    try:
        passer = TemplateConfigFormat.do_batchfile_parse_config(config_path)
    except Exception as e:
        console.print(Panel.fit(f"[bold red]Document config file reading has failed: {str(e)}", title="Error occurs"))
        raise typer.Exit()
    process_batch_by_arg_passer(passer, req_ensure)


@app.command()
def gen_sf_config(
    config_path: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIG_GEN_STR, prompt=CLICommandHelper.CONFIG_GEN_PROMPT)],
    config_type: Annotated[
        str, typer.Option(help=CLICommandHelper.CONFIGTYPE_GEN_STR, prompt=CLICommandHelper.CONFIGTYPE_GEN_PROMPT)]
):
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
    if config_type not in TemplateConfigFormat.supportive_format():
        console.print(Panel.fit(
            f"[bold red]The format you pass {config_type} is not supported!"\
            "see the supportive configs: "
            , title="Error occurs"))
        format_file_list()
    TemplateConfigFormat.generate_file_accord_type(config_type, config_path, TemplateConfigFormat.DOC_TREE_TYPE)
    



@app.command()
def langs_list():
    console.print(Panel.fit(DocumentTranslatorCLI.def_engine_lang_supports(), title="Support languages"))

@app.command()
def format_file_list():
    console.print(Panel.fit(TemplateConfigFormat.display_support_format_string(), title="Support config format file"))

if __name__ == "__main__":
    app()