DPATH=$(realpath "$(dirname "${BASH_SOURCE[0]}")")
VERSION=`docker inspect -f {{.Config.Labels.version}} nodejsscan-cli`
#echo $VERSION
mkdir -p $DPATH/../test-src/tmp && chmod 0777 $DPATH/../test-src/tmp
start=$SECONDS
docker run -u nodejsscan -v $DPATH/../test-src:/usr/src/app/test-src nodejsscan-cli -d /usr/src/app/test-src -o /usr/src/app/test-src/tmp/results.json
end=$SECONDS
let diff=(end-start)*1000
python3 $DPATH/../transform.py -i $DPATH/../test-src/tmp/results.json -o $DPATH/../output.json -v $VERSION -t $diff 

