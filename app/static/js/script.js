var data1=[];
var datapart=[];
var x=0;
var y=0;
var textx="";
var texty="";
var textteta="";
var textqtype="";


async function senddata(){
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

    for(i=0;i<data1.length;i++){
        var paire=[data1[i][0],data1[i][1]];
        const result = await global_ubqc.send_plus_theta(paire,data1[i][2]);
    }
}

async function send_entanglement_graph() {
    var cz_list = []
    for (i=0; i< tab2var;i++){
        // Get all values for this line
        x1=parseInt(document.getElementById("tab2x1"+i).value);
        y1=parseInt(document.getElementById("tab2y1"+i).value);
        x2=parseInt(document.getElementById("tab2x2"+i).value);
        y2=parseInt(document.getElementById("tab2y2"+i).value);
        // Add to cz_list
        cz_list.push([[x1, y1], [x2, y2]]);
    }
    const result = await global_ubqc.send_CZ_list(cz_list);
}
