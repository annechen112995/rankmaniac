#!/usr/local/bin/perl -w

$iters = 0;

$out1 = "output.txt";
$out2 = "output2.txt";

system('python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt');

while ($iters < 50)
{
    open DATA1, "$out1";
    open DATA2, "$out2";
    if ((grep {/Final/} <DATA1>) or (grep {/Final/} <DATA2>)) {
	    print 'done';
	    exit(0);
    }
    close DATA1;
    close DATA2;

    if ($iters % 2 == 0)
    {
        system('python pagerank_map.py < output.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output2.txt');
        print $iters;
        $iters++;
    }
    else
    {
        system('python pagerank_map.py < output2.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt');
        print $iters;
        $iters++;
    }
}