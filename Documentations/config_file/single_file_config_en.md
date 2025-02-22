# Configuration file description

This is a single document translation configuration file. The following fields must be specified:

- `src_doc`: Source document path
- `dest_lang`: Target language
- `split_colon`: Separator setting

Other fields will use default values.

## Configuration file field description

### [type]

- `anatype`: Specify the document type, which must be set to `single-file` to represent a single document translation.

### [document_path]

- `src_doc`: Source document path. This field specifies the location of the source document to be translated.
- `dest_doc`: target document path. This field specifies the translated document storage location.

### [langs_settings]

- `dest_lang`: Target language. This field specifies the target language for the translation document.
- `split_colon`: Delimiter setting. Specifies whether to use a colon as a separator for translation content. Usually a boolean value or a string.

## Sample configuration file

```
[type]
anatype = single-file

[document_path]
src_doc = /path/to/source/document.txt
dest_doc = /path/to/destination/translated_document.txt

[langs_settings]
dest_lang = en
split_colon = .
```

In the above example:

- The source document `/path/to/source/document.txt` will be translated.
- The translated document will be saved as `/path/to/destination/translated_document.txt`.
- Translate the target language to `en` (English) and take the Chinese full stop. As a separator