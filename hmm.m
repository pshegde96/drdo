clear all;clc;

TRANS = [0.9 0.1;0.05 0.95];
EMIS = [1/6 1/6 1/6 1/6 1/6 1/6;7/12 1/12 1/12 1/12 1/12 1/12];

[seq,states] = hmmgenerate(1000,TRANS,EMIS);

likelystates = hmmviterbi(seq,TRANS,EMIS);
sum(states == likelystates)/1000;

[TRANS_EST,EMIS_EST] = hmmestimate(seq,states);
TRANS
TRANS_EST
EMIS
EMIS_EST