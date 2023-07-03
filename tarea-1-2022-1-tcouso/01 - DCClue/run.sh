while getopts n: flag
do
    case ${flag} in
        n) n_prob=${OPTARG};;
    esac

done
clingo maps/map1.lp problems/prob${n_prob}.lp detective.lp | python3 process.py