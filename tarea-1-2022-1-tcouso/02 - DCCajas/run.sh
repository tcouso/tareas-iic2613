while getopts n: flag
do
    case ${flag} in
        n) n_prob=${OPTARG};;
    esac

done
clingo problems/prob${n_prob}.lp robots.lp | python3 process.py
# clingo problems/prob${n_prob}.lp | python3 process.py
# clingo robots.lp | python3 process.py
