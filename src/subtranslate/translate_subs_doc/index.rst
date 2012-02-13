Subtitle Translator
===================

Google Translate api doesn't support free translations now. So, this subtitle translator uses **mygengo** and able to translate subtitles using terminal and a mygengo free account to translate subtitles in various supported Langauges. Supported file format is ``srt`` in ``UTF-8`` Format. This application is written in Python and script **translate_subs** is installed in your main shell.

Pre-requisites
--------------

1. `mygengo <http://pypi.python.org/pypi/mygengo/1.3.1>`_ 

No need to installed as it is installed automatically as dependencies. However, incase of troubles install mygengo manually

2. Python 2.6.* or above

3. `mygengo api registration <http://mygengo.com>`_

Obtain
------

::

  git clone git://kevincobain2000@github.com/kevincobain2000/subtitle_translator.git

Install
-------

``python setup.py install``


Install Keys
------------

  1. Register at ``mygengo`` and installing ``mygengo python api``.
  2. Generate public_key and private_key.
  3. Make a dir in your home directory like this ``mkdir ~/mygengo_keys``
  4. Copy and Paste and save in the files ``~/mygengo_keys/public_key.txt`` and ``~/mygengo_keys/private_key.txt``, respectively.
  5. Save the above text files in home directory. `Note#` Do ``echo $HOME`` to find out location of your home directory.

Usage
-----

Script ``translate_subs`` is installed and is called directly.
::

  1. translate_subs -i input.srt -f english -t japanese
  2. translate_subs -i input.srt -f en -t ja
  3. translate_subs -i input.srt -f Eng -t Jap

>>> Output --> Translated file saved to ja-input.srt

Supported Languages
-------------------

::

  sv        Swedish
  id        Indonesian
  pt        Portuguese (Europe)
  es-la     Spanish (Latin America)
  ko        Korean
  ar        Arabic
  fr-ca     French (Canada)
  nl        Dutch
  en        English
  ja        Japanese
  es        Spanish (Spain)
  zh        Chinese (Simplified)
  de        German
  fr        French
  ru        Russian
  it        Italian
  pt-br     Portuguese (Brazil)

`Note#` Supported Languages are from English to Target language and vice versa

Charset
-------

``input.srt`` file must be ``utf-8`` encoded. To convert to ``utf-8`` see ``man iconv``

Help
----

``translate_subs -h``

Contact
-------

  1. `Home <http://www.jaist.ac.jp/~s1010205/>`_

  2. `Contact Form <http://www.jaist.ac.jp/~s1010205/styled-2/index.html>`_

  3. `github <https://github.com/kevincobain2000/subtitle_translator>`_
  
  4. ``pulkit[at]jaist.ac.jp``
 
