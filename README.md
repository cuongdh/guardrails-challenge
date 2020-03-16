# Security Engineer Challenge Answer
**Candidate:** Cuong H. Dinh - dhcuong@outlook.com
> This repository contains the answer to challenge for the security engineers of GuardRails.

## Engine Exercise

The engine exercise is contained in this repository, with the following structure:

```bash
├──build/ #where souce code of NodeJSScan cloned from its repo, triggered by tools/build.sh
├──test-src/ #contains source code of NodeGoat
├──tools/ #contains bash tool
├────build.sh #bash script to clone the NodeJSScan repo then build the docker image
├────run.sh #bash script to run the container (nodejssca-cli) from built image and execute the transform.py
├──Dockerfile #Dockerfile which been used to build nodejsscan-cli (minimized version of NodeJSScan running in CLI)
└──transform.py #python3 script which used to transform the output from nodejsscan-cli to new json format required by challenge
```
## Code Explain
1. The `Dockerfile` using alpine linux and nodejsscan-cli version for simplest and smallest image. Running user/group which been defined in non-root nodejsscan/nodejsscan, stricted to /usr/src/app folder.
1. `tools/build.sh` this bash script will be using to download NodeJSScan from original repo to `build\` and and build the image from customized Dockerfile.
The version of NodeJSScan also being labeled as `version` label in image for engine version info at outut
1. `tools/run.sh` this bash script used for getting `version` label, and trigger container start, execute the scanning and time measuring. Finally, start `transform.py`
1. `transform.py` will do the transforming from NodeJSScan output to required format.

## Objectives

The objective of this challenge is to containerize [NodeJsScan](https://github.com/ajinabraham/NodeJsScan) and transform the output of the tool to the following structure:

```js
{
  "engine": {
    "name": "guardrails/engine-javascript-nodejsscan",
    "version": "1.0.0"
  },
  "process": {
    "name": "nodejsscan ",
    "version": "3.4"
  },
  "language": "javascript",
  "status": "success",
  "executionTime": 212, //in milliseconds
  "issues": 10, // number of identified issues
  "output": [
    // array containing all identified issues
    {
      "type": "sast", // This is static
      "ruleId": "Server Side Injection(SSI) - eval", // this is the title of the issue
      "location": {
        "path": "app/routes/contributions.js", // path to the file where the issue was identified
        "positions": {
          "begin": {
            "line": 26 // line number where the issue was identified
          }
        }
      },
      "metadata": {
        "description": "User controlled data in eval() can result in Server Side Injection (SSI) or Remote Code Execution (RCE)."
      }
    } // [...]
  ]
}
```

