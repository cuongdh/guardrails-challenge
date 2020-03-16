#!/usr/bin/python3
import re, sys, getopt, json,os

def main(argv):
    idir = os.getcwd()
    buffer = []
    try:
        opts, args = getopt.getopt(argv,"h:i:o:v:t:",["ifile=","ofile=","version","time",])
    except getopt.GetoptError:
        print ('transform.py -i <inputfile> -o <outputfile> -v <engine_version> -t <exec_time>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('transform.py -i <inputfile> -o <outputfile> -v <engine_version> -t <exec_time>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputJSON = arg
        elif opt in ("-o", "--ofile"):
            outputJSON = arg
        elif opt in ("-v", "--version"):
            engineVersion = arg
        elif opt in ("-t", "--time"):
            execTime = arg
    with open(inputJSON, "r") as read_file:
        data = json.load(read_file)
        vulns = data['sec_issues']
        for key, value in vulns.items():
            for i in range(len(vulns[key])):
                issue = {"type": "sast", "ruleId": vulns[key][i]['title'], "location": {}}
                issue["location"]["path"] = vulns[key][i]['path'].replace("/usr/src/app", idir)
                issue["location"]["positions"] = {"begin": {"line": vulns[key][i]['line']}}
                issue["metadata"] = {"description": vulns[key][i]["description"]}
                buffer.append(issue)
        export = {"engine": {}}
        export["engine"]["name"] = "guardrails/engine-javascript-nodejsscan"
        export["engine"]["version"] = "1.0.0"
        export["process"] = {}
        export["process"]["name"] = "nodejsscan "
        export["process"]["version"] = engineVersion
        export["language"] = "javascript"
        export["status"] = "success"
        export["executionTime"] = execTime
        export["issues"] = data['total_count']['sec']
        export["output"] = buffer
        json_object = json.loads(json.dumps(export))
        json_formatted_str = json.dumps(json_object, indent=2)
        fopen = open(outputJSON, "w")
        fopen.writelines(json_formatted_str)
        fopen.close()
if __name__ == "__main__":
    main(sys.argv[1:])
