# Anki Translator Add-on
# Helps creating vocabulary flashcards by searching for translations on the web.
#
# https://github.com/jannewulf/Anki-Translator
# jannewulf@gmail.com
#
# Copyright (C) 2016  Janne Wulf
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import TranslatorAddon.core as core

# Here you can set the default Languages.
# For available Language Codes you can see TranslatorAddon/Parser/pons_lang_codes.xml
core.defaultSourceLanguage = "en"
core.defaultTargetLanguage = "de"
core.defaultLoadGrammarInfos = False

core.init()