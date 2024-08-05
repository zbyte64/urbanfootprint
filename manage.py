#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    # Using production settings: override with --settings=footprint.settings_dev to get the default
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "footprint.settings_prod")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
