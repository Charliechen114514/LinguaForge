# Configuration file description

The main purpose of this configuration file is to facilitate batch file translation operations and ensure that source documents and translation results are stored in the specified format and path. In the configuration, the following fields must be specified:

* `src_doc`: Source document path
* `dest_lang`: Target language
* `split_colon`: Separator setting

Other fields can use default values ​​(not filled in). For batch file generation, the generation type must be specified:

* `all-in-one`: Summary of the translation files to the specified root directory.
* `insert-in`: Generate the translation file to the directory of the original document at the same level.

## Configuration file field description

### [type]

* `anatype`: Specify the document type, usually `doc-tree`. This field is used to specify the structure type of the document. **Please do not modify this field**

### [document_path]

* `src_dir`: The directory path where the source document is located.
* `dest_type`: Please specify one of the following options, otherwise an error will be reported during parsing
  * `all-in-one`: Summary of the translation files to the specified root directory.
  * `insert-in`: Generate the translation file to the directory of the original document at the same level.
* `dest_dir`: The target directory where the translation file will be stored.
* `check_suffix`: Set the suffix name of the scan

### [langs_settings]

* `dest_lang`: Settings of the target language, used to specify the language of the translation result.
* `split_colon`: Specifies whether to split the translation content using a colon, usually a boolean or a string.

## Sample configuration file

# Configuration file example, configuring source documents and target translation settings

```
[type]
anatype = doc-tree

[document_path]
src_dir = /path/to/source/docs
dest_type = all-in-one
dest_dir = /path/to/destination/docs
check_suffix = md

[langs_settings]
dest_lang = en
split_colon = .
```

In the above example:

* The source document is stored in the `/path/to/source/docs` directory. When specified as all-in-one, it will be generated under the /path/to/destination/docs you specified.
* The format of the translation file is `md`, which will mean that only all md documents in the directory will be collected.
* The target language is set to `en` (English) and takes a Chinese period. As a separation, it can improve the quality of translation more accurately.