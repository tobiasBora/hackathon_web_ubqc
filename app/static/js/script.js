var data=[];
var datapart=[];
var x=0;
var y=0;
var textx="";
var texty="";
var textteta="";
var textqtype="";

function senddata(){
    for (i=1; i<= tab1var;i++){
        textx="x"+i;
        texty="y"+i;
        textteta="random"+i;
        textqtype="qtype"+i;
        x=document.getElementById(textx).value;
        xint=parseInt(x);
        y=document.getElementById(texty).value;
        yint=parseInt(y);
        teta=document.getElementById(textteta).innerHTML;
        tetaint=parseInt(teta);
        qtype=document.getElementById(textqtype).value;
        var datapart=[];
        datapart.push(xint,yint,tetaint,qtype);
        data[i-1]=datapart;
    }

    for(i=0;i<data.length;i++){
        var paire=(data[i].x,data[i].y);
        send_plus_theta(paire, data[i][2]);
    }
}

