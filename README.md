## RPGMakerUtil

### JSONFormat

Format `RPGMaker` engine `JSON` file in `data` dir, support MV & MZ.

##### Example

    {"id":1,"value":"Hello,\u0020\u0077\u006F\u0072\u006C\u0064\u0021"}
    ↓
    {
        "id": 1,
        "value": "Hello, world!"
    }

##### Usage

place JSONFormat.py same level as the `data` dir and run it.

### Supported

python3
