var data1=[];
var datapart=[];
var x=0;
var y=0;
var textx="";
var texty="";
var textteta="";
var textqtype="";



function tabQubit(){
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
        data1[i-1]=datapart;
    }
    return data1
}


async function senddata(){
    const dataQ=tabQubit(); 
    for(i=0;i<dataQ.length;i++){
        var paire=[dataQ[i][0],dataQ[i][1]];
        const result = await global_ubqc.send_plus_theta(paire,dataQ[i][2]);
    }
}

async function send_entanglement_graph() {

    var selected=[];
    var  eachToSplit1="";
    var  eachToSplit2="";
    for (i=0; i< tab2var;i++){
        eachToSplit1=document.getElementById("tab21"+i).value;
        eachToSplit2=document.getElementById("tab22"+i).value;
        var eachSplitted1=eachToSplit1.split(';');
        var eachSplitted2=eachToSplit2.split(';');
        eachSplitted1.push([])
        selected.push([ [eachSplitted1[0],eachSplitted1[1]] ,[eachSplitted2[0],eachSplitted2[1]] ] );
    }
    const result = await global_ubqc.send_CZ_list(selected);
}


