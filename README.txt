fora README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/create_fora_instance -s <scaffold> <instance directory>

- cd <instance directory>

- $VENV/bin/initialize_fora_db development.ini

- $VENV/bin/pserve development.ini

i18n
----
extract strings

- cd <directory containing this file>

- $VENV/bin/pot-create -o fora/locales/fora.pot fora

generate fora.po for target language

- cd <directory containing this file>

- cd fora/locales

- msginit -l LANG_CODE -o LANG_CODE/LC_MESSAGES/fora.po
