param (
    [string]$command
)

switch ($command) {
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