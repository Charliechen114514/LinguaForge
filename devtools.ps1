param (
    [string]$command
)

switch ($command) {
    # Open the designer 
    "--setup" {
        Write-Host "Setup the neccessities"
        poetry install
        Write-Host "Setup the neccessities down"
    }

    "--open_designer" {
        Write-Host "Opening Designer..."
        poetry run python .\dev_tools\open_designer.py
    }

    # summon the ui file
    "--summon_uipy" {
    }

    "--summon_rccpy" {
    }

    # run the main applications
    "--run" {   
        Write-Host "Start Main CLI Creations..."
        poetry run python -m linguaforge.main
    }

    "--prepare"{
    }

    "--all"{
        devtools.ps1 --prepare
        devtools.ps1 --run
    }

    "--clean"{
        Write-Host "Cleaning the sources..."
        poetry run python -m devtools.clean
        Write-Host "Clean up down"
    }

    "--test"{
        Write-Host "Test the main functionalities..."
        poetry run pytest
        Write-Host "Test Down!"
    }

    "--help"{
        Write-Host 

    "Usage: devtools.ps1 [OPTIONS]

    Options:
        --setup                Setup the environment, which will install the dependencies automatically
        --open_designer        Open Designer and launch the Designer application.
        --summon_uipy          Summon UI from the .ui file and transform it into the UI Python code.
        --run                  Run the main application directly.
        --prepare              Set up environments for the main application and perform necessary transformations.
        --all                  Set up environments and run the main application.
        --help                 Show this help message and exit.
        --clean                Clean up the runtime middlewares and the pycaches
        --test                 Test the functionalities if required
        "  
        
    }

    default {
        Write-Host "Unknown command. Please use one of the following:"
        dev_tools.ps1 --help
    }
}