PROGNAME="SentencePieceMicroS"
RELEASE="Revision 1.0"
AUTHOR="(c) 2021 Aubertin Emmanuel"
DEBUG=0

# Functions plugin usage
print_release() {
    echo "$RELEASE $AUTHOR"
}

print_usage() {
        echo ""
        echo "$PROGNAME"
        echo ""
        echo "Usage: $PROGNAME | [-h | --help] | [-v | --version] | [-d | --debug]"
        echo ""
        echo "          -h  Aide"
        echo "          -v  Version"
        echo ""
        echo "This project is a web ui for llama.cpp"
}

print_help() {
        print_release $PROGNAME $RELEASE
        echo ""
        print_usage
        echo ""
        echo ""
                exit 0
}


while [ $# -gt 0 ]; do
    case "$1" in
        -h | --help)
            print_help
            exit 
            ;;
        -v | --version)
            print_release
            exit 
            ;;                          
        *)  echo "Unkown argument: $1"
            print_usage
            ;;
        esac
shift
done

echo "#### CHECKING FOR DEP"
echo "## API DEP"
python3 -m pip install fastapi sentencepiece pydantic google-auth requests PyJWT

