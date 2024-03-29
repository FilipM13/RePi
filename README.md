![base](https://github.com/FilipM13/RePi/actions/workflows/base.yml/badge.svg)
# RePi

## High level overview

<img src="https://github.com/FilipM13/RePi/blob/main/README/ReportPipeline.jpg">

This project will contain 3 components.
1. RePiCore - Main Python library responsible for all processing (creating and executing pipeline).
2. RePiReader - Python library responsible for reading text files and converting them to RePiCore pipeline.
3. RePiWeb - Django based application (web or desktop) that will provide GUI for creating and executing pipelines.

Action table:
1. Repo setup 
(<a href="https://github.com/FilipM13/RePi/milestone/1">milestone<a/>):
:white_check_mark:
   1. creating src and tests directories :white_check_mark:
   2. creating mypy configuration :white_check_mark:
   3. creating flake8 configuration :white_check_mark:
   4. creating pytest configuration :white_check_mark:
   5. creating black formatting configuration :white_check_mark:
   6. creating project config files (setup.py) :white_check_mark:
   7. creating basic CI/CD pipelines :white_check_mark:
2. Developing RePiCore 
(<a href="https://github.com/FilipM13/RePi/milestone/2">milestone<a/>): 
:arrow_forward:
   1. basic diagram :white_check_mark:
   2. creating classes :hammer:
   3. testing classes :arrow_forward:
   4. creating sample pipelines :arrow_forward:
   5. testing pipelines :arrow_forward:
   6. documenting module
3. Developing RePiReader 
(<a href="https://github.com/FilipM13/RePi/milestone/3">milestone<a/>):
:no_entry:
   1. choosing file format
   2. creating interpreter
   3. testing interpreter
   4. documenting module
4. Developing RePiWeb 
(<a href="https://github.com/FilipM13/RePi/milestone/4">milestone<a/>): 
:no_entry:
   1. learning Django and React
   2. creating diagram
   3. developing basic web app structure
   4. developing "app guts" (for lack of better term at the moment)
   5. testing app
   6. documenting app
   7. delivering app
5. Possibly public release 
:no_entry:

Statuses:<br>
:no_entry: - blocked <br>
:arrow_forward: - ongoing <br>
:hammer: - testing <br>
:white_check_mark: - complete <br>

## RePiCore

### High level overview

<img src="https://github.com/FilipM13/RePi/blob/main/README/RePiCore.jpg">

RePiCore is split into 5 basic layer with 5 interface classe as a base. 
1. Source interface class for all classes acting as input.
2. Operation interface class for all classes that will function as data manipulators.
3. ReportElement interface class for all classes that can be displayed in output file.
4. Report interface class for all classes responsible for rendering output document.
5. Package interface class for all classes that allow grouping output documents.

