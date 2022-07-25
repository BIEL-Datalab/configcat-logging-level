# configcat-logging-level

## Getting started
```
# install configccat python client
pip install git+https://github.com/BIEL-Datalab/configcat-logging-level.git@master
```

## Settings
- `CONFIGCAT_SDK[str]`  Your ConfigCat SDK to control logging level. https://configcat.com/docs/sdk-reference/overview/
- `FEATURE_FLAG_NAME[str]` The variable name to control logging level which setting in ConfigCat, default to `LOGGER_LEVEL`.
- `CANFIGCAT_POLL_INTERVAL_SECONDS[int]` The interval ConfigCat SDK downloads the latest values and stores them automatically, default to 60.
- `EXECUTION_ENV[str]` The execution environment, default to `default`, if the value is one of the `k8s`, `bastion`, `test`, `default`, it will create a real configcat_client, or would mock it. And the return value would be `MOCK_LOGGING_LEVEL` which default to `default`.
- `MOCK_LOGGING_LEVEL[str]` The mock return value of mock configcat_client, default to `default`.
## Usage
```
from configcat_logging_level import logging_controller
logging_controller.create()
```


