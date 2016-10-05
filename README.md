# Anki-Translator
######v1.1
Anki-Translator is a Add-On for the flashcard program [Anki](http://ankisrs.net/).

This Add-On translates vocabularies for you. So if you want to add a new flashcard to your deck you can open this Add-On 
and let it find translations for you from the web.

All the Translations come from [PONS](http://en.pons.com/).

### Available Languages (Not all combinations):
* Arabic
* Chinese
* Dutch
* English
* French
* German
* Greek
* Italian
* Latin
* Polish
* Portuguese
* Russian
* Slovenian
* Spanish
* Turkish
* Czech
* Danish
* Hungarian
* Norwegian
* Swedish
* Elvish

## Usage
![alt tag](https://raw.githubusercontent.com/jannewulf/Anki-Translator/master/docs/Button.png)

Just click this translate button in Anki's Editor. 

![alt tag](https://raw.githubusercontent.com/jannewulf/Anki-Translator/master/docs/translated-tree.png)

A new window opens where you choose the source and target languages and if you want grammar infos (like grammatical
gender, etc.).

After you entered the vocable and clicked on 'Translate' the translations get loaded. You mark the checkboxes of the 
translations you want to have on your flashcard and leave the window with a click on 'OK'.

The chosen translations get copied on your flashcard.

## Default Values
You can change the default values for source and target language and also for the grammar infos. Just change the values 
of the variables in the file 'Translator.py'. You can find the file in the Add-Ons Folder of your Anki Installation.

![alt tag](https://raw.githubusercontent.com/jannewulf/Anki-Translator/master/docs/settings.png)

(See the highlighted lines.)

## Installation
This Add-On is also posted on the [Anki Add-Ons Website](https://ankiweb.net/shared/info/300631469/). You can use the Add-On Installer, which is integrated into Anki, to install the Translator. 
The Downloadcode is '300631469'.

Or you can download this project and copy the 'Translator.py' file and the 'TranslatorAddon' folder into your Anki Add-On directory.
