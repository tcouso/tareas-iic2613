while getopts n: flag
do
    case ${flag} in
        n) n_prob=${OPTARG};;
    esac

done
clingo problems/prob${n_prob}.lp robots.lp