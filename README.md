# fora

fora is a WSGI framework for forums.

## Getting Started ##
<code>cd directory_containing_this_file</code>

<code>$VENV/bin/python setup.py develop</code>

<code>$VENV/bin/create_fora_instance -s scaffold_name instance_directory</code>

<code>cd instance_directory</code>

<code>$VENV/bin/initialize_fora_db development.ini</code>

<code>$VENV/bin/pserve development.ini</code>

## i18n ##
extract strings

<code>cd directory_containing_this_file</code>

<code>$VENV/bin/pot-create -o fora/locales/fora.pot fora</code>

generate fora.po for target language

<code>cd directory_containing_this_file</code>

<code>cd fora/locales</code>

<code>msginit -l LANG_CODE -o LANG_CODE/LC_MESSAGES/fora.po</code>
