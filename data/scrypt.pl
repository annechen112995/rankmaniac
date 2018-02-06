#!/usr/local/bin/perl -w

$iters = 0;

my $out1 = "output.txt";
open DATA1, "$out1";
my $out2 = "output2.txt";
open DATA2, "$out2";

system('python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt');

while ($iters < 9)
{
    if (grep {/Final/} <DATA1>) {
	    print 'done';
	    exit(0);
    }
    if ($iters % 2 == 0)
    {
        system('python pagerank_map.py < output.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output2.txt');
	if (grep{/Final/} <DATA2>) {
	    print 'done';
	    exit(0);
	}
        print $iters;
        $iters++;
    }
    else
    {
        system('python pagerank_map.py < output2.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt');
	if (grep{/Final/} <DATA1>) {
	    print 'done';
	    exit(0);
	}
        print $iters;
        $iters++;
    }
}

close DATA1;
close DATA2;