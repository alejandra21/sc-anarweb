// Este archivo actualmente no se utiliza, el JS de la rueda está dentro del
// mismo html para aprovechar las utilidades de django con el direccionamiento
// de la página.

$(document).ready(function(){
var angle = 0;
var angle2 = 0;
	var margin =$("#cara1").width()/2;
	var width=$("#cara1").width();
	var height=$("#cara1").height();
	var margintapa =$("#tapauno").width()/2;
	var widthtapa=$("#tapauno").width();
	var heighttapa=$("#tapauno").height();
	var marginzoom1 =$("#zoom1").width()/2;
	var widthzoom1=$("#zoom1").width();
	var heightzoom1=$("#zoom1").height();
	var marginzoom2=$("#zoom2").width()/2;
	var widthzoom2=$("#zoom2").width();
	var heightzoom2=$("#zoom2").height();
	var marginzoom3 =$("#zoom3").width()/2;
	var widthzoom3=$("#zoom3").width();
	var heightzoom3=$("#zoom3").height();
	var marginzoom4 =$("#zoom4").width()/2;
	var widthzoom4=$("#zoom4").width();
	var heightzoom4=$("#zoom4").height();
	var marginzoomtit =$("#zoomtit").width()/2;
	var widthzoomtit=$("#zoomtit").width();
	var heightzoomtit=$("#zoomtit").height();
	var marginzoomparte =$("#zoomparte").width()/2;
	var widthzoomparte=$("#zoomparte").width();
	var heightzoomparte=$("#zoomparte").height();
	var marginzoomrupestre =$("#zoomrupestre").width()/2;
	var widthzoomrupestre=$("#zoomrupestre").width();
	var heightzoomrupestre=$("#zoomrupestre").height();
	var marginzoomarte =$("#zoomarte").width()/2;
	var widthzoomarte=$("#zoomarte").width();
	var heightzoomarte=$("#zoomarte").height();
	var count=0;
	var visib=0;
	var ubicacionV=0;
	var ubicacionM=0;

$("#manoizq").click(function(){


if(count==0){
	
		
		angle-=45;
		console.log(angle)
		$("#cara1").rotate({ animateTo: angle});
		ubicacionV-=1;
		if (ubicacionV==-8)
		{
			ubicacionV=0;
		}
		
	}
	else{
		angle2-=45;
		$("#cara2").rotate({ animateTo: angle2});
		ubicacionM-=1;
		if (ubicacionM==-8)
		{
			ubicacionM=0;
		}
	}
});
$("#manoder").click(function(){
	

	if(count==0){
		angle+=45;
		$("#cara1").rotate({ animateTo: angle});
		ubicacionV+=1
	if (ubicacionV==8)
		{
			ubicacionV=0;
		}
	}
	else{
		angle2+=45;
		$("#cara2").rotate({ animateTo: angle2});
		ubicacionM+=1
	if (ubicacionM==8)
		{
			ubicacionM=0;
		}
	}
});

	$("#girarrueda").click(function(){
		if(count==0){
			count=1;		

		$("#cara1").stop().animate({width:'0px',height:''+height+'px',marginLeft:''+margin+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#cara2").stop().animate({width:''+width+'px',height:''+height+'px',marginLeft:'0px',opacity:'1'},{duration:500});
		},500);
		
		$("#tapauno").stop().animate({width:'0px',height:''+heighttapa+'px',marginLeft:''+margintapa+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#tapados").stop().animate({width:''+widthtapa+'px',height:''+heighttapa+'px',marginLeft:'125px',opacity:'1'},{duration:500});
		},500);
		
		$("#zoom1").stop().animate({width:'0px',height:''+heightzoom1+'px',marginLeft:''+marginzoom1+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom1").stop().animate({width:''+widthzoom1+'px',height:''+heightzoom1+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom2").stop().animate({width:'0px',height:''+heightzoom2+'px',marginLeft:''+marginzoom2+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom2").stop().animate({width:''+widthzoom2+'px',height:''+heightzoom2+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom3").stop().animate({width:'0px',height:''+heightzoom3+'px',marginLeft:''+marginzoom3+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom3").stop().animate({width:''+widthzoom3+'px',height:''+heightzoom3+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom4").stop().animate({width:'0px',height:''+heightzoom4+'px',marginLeft:''+marginzoom4+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom4").stop().animate({width:''+widthzoom4+'px',height:''+heightzoom4+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoomtit").stop().animate({width:'0px',height:''+heightzoomtit+'px',marginLeft:''+marginzoomtit+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomtit").stop().animate({width:''+widthzoomtit+'px',height:''+heightzoomtit+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoomparte").stop().animate({width:'0px',height:''+heightzoomparte+'px',marginLeft:''+marginzoomparte+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomparte").stop().animate({width:''+widthzoomparte+'px',height:''+heightzoomparte+'px',marginLeft:'150px',opacity:'1'},{duration:500});
		},500);
		$("#zoomarte").stop().animate({width:'0px',height:''+heightzoomarte+'px',marginLeft:''+marginzoomarte+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomarte").stop().animate({width:''+widthzoomarte+'px',height:''+heightzoomarte+'px',marginLeft:'375px',opacity:'1'},{duration:500});
		},500);	
		$("#zoomrupestre").stop().animate({width:'0px',height:''+heightzoomrupestre+'px',marginLeft:''+marginzoomrupestre+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomrupestre").stop().animate({width:''+widthzoomrupestre+'px',height:''+heightzoomrupestre+'px',marginLeft:'390px',opacity:'1'},{duration:500});
		},500);	
	$("#ImgToTitulo").attr("src", "static/site/ruedadidactica/img/mundorupestre.png") ;
	}
	else{
		count=0;
		$("#cara2").stop().animate({width:'0px',height:''+height+'px',marginLeft:''+margin+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#cara1").stop().animate({width:''+width+'px',height:''+height+'px',marginLeft:'0px',opacity:'1'},{duration:500});
		},500);
		
	$("#tapados").stop().animate({width:'0px',height:''+heighttapa+'px',marginLeft:''+margintapa+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#tapauno").stop().animate({width:''+widthtapa+'px',height:''+heighttapa+'px',marginLeft:'120px',opacity:'1'},{duration:500});
		},500);
		
		$("#zoom1").stop().animate({width:'0px',height:''+heightzoom1+'px',marginLeft:''+marginzoom1+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom1").stop().animate({width:''+widthzoom1+'px',height:''+heightzoom1+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom2").stop().animate({width:'0px',height:''+heightzoom2+'px',marginLeft:''+marginzoom2+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom2").stop().animate({width:''+widthzoom2+'px',height:''+heightzoom2+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom3").stop().animate({width:'0px',height:''+heightzoom3+'px',marginLeft:''+marginzoom3+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom3").stop().animate({width:''+widthzoom3+'px',height:''+heightzoom3+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoom4").stop().animate({width:'0px',height:''+heightzoom4+'px',marginLeft:''+marginzoom4+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoom4").stop().animate({width:''+widthzoom4+'px',height:''+heightzoom4+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoomtit").stop().animate({width:'0px',height:''+heightzoomtit+'px',marginLeft:''+marginzoomtit+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomtit").stop().animate({width:''+widthzoomtit+'px',height:''+heightzoomtit+'px',marginLeft:'263px',opacity:'1'},{duration:500});
		},500);
		$("#zoomparte").stop().animate({width:'0px',height:''+heightzoomparte+'px',marginLeft:''+marginzoomparte+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomparte").stop().animate({width:''+widthzoomparte+'px',height:''+heightzoomparte+'px',marginLeft:'150px',opacity:'1'},{duration:500});
		},500);
		$("#zoomarte").stop().animate({width:'0px',height:''+heightzoomarte+'px',marginLeft:''+marginzoomarte+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomarte").stop().animate({width:''+widthzoomarte+'px',height:''+heightzoomarte+'px',marginLeft:'375px',opacity:'1'},{duration:500});
		},500);
		$("#zoomrupestre").stop().animate({width:'0px',height:''+heightzoomrupestre+'px',marginLeft:''+marginzoomrupestre+'px',opacity:'0.5'},{duration:500});
		window.setTimeout(function() {
		$("#zoomrupestre").stop().animate({width:''+widthzoomrupestre+'px',height:''+heightzoomrupestre+'px',marginLeft:'390px',opacity:'1'},{duration:500});
		},500);
	$("#ImgToTitulo").attr("src", "img/vzlarupestre.png") ;
	}
	
		
	});
	
	$("#zoomtit").hover(function(){
			$("#DivImgToZoom").css('margin-left','830px');
	$("#ImgToZoom").attr("src", "zooms/logo.png") ;
		if(visib==0){
			visib=1;
			$("#ImgToZoom").css('height','264px');		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
	});

$("#zoomparte").hover(function(){
			$("#DivImgToZoom").css('margin-left','830px');
if(count==0)
		{
		$("#ImgToZoom").attr("src", "zooms/vzla.png") ;
		}
else{
		$("#ImgToZoom").attr("src", "zooms/mund.png") ;
		}
		if(visib==0){
			visib=1;
			$("#ImgToZoom").css('width','217px');			
			$("#ImgToZoom").css('height','409px');		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
	});

$("#zoomrupestre").hover(function(){
			$("#DivImgToZoom").css('margin-left','830px');
if(count==0)
		{
		$("#ImgToZoom").attr("src", "zooms/vzlarup.png") ;
		}
else{
		$("#ImgToZoom").attr("src", "zooms/mundrup.png") ;
		}
		if(visib==0){
			visib=1;
			$("#ImgToZoom").css('width','217px');			
			$("#ImgToZoom").css('height','409px');		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
	});



	$("#zoom1").hover(function(){
		$("#ImgToZoom").css('height','200px');
		$("#ImgToZoom").css('width','300px');
		$("#DivImgToZoom").css('margin-left','830px');
		if(count==0)
			{
				
			switch(ubicacionV){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/SEVCerroGuarani.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/SEVSantaAnita.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/SEVOnoto.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/SEVChirgua.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/SEVSaltoParu.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/SEVCerroCuevaIglesias.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/SEVVigirima.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/SEVChipaque.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/SEVSantaAnita.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/SEVOnoto.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/SEVChirgua.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/SEVSaltoParu.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/SEVCerroCuevaIglesias.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/SEVVigirima.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/SEVChipaque.png") ;
				break;
			
			}	
			}	
			
			else{
			switch(ubicacionM){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/SEMCostaRica.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/SEMFrancia.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/SEMInglaterra.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/SEMIndia.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/SEMNamibia.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/SEMAustralia.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/SEMPeru.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/SEMUsa.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/SEMFrancia.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/SEMInglaterra.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/SEMIndia.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/SEMNamibia.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/SEMAustralia.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/SEMPeru.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/SEMUsa.png") ;
				break;
			
			}	
				
			
			}
		if(visib==0){
			visib=1;		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
			
		
		
		});
		
	$("#zoom2").hover(function(){
			$("#ImgToZoom").css('height','200px');
			$("#ImgToZoom").css('width','300px');
		$("#DivImgToZoom").css('margin-left','830px');
		if(count==0)
			{
				
			switch(ubicacionV){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/FigVCerroGuarani.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/FigVSantaAnita.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/FigVOnoto.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/FigVChirgua.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/FigVSaltoParu.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/FigVCerroCuevaIglesias.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/FigVVigirima.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/FigVChipaque.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/FigVSantaAnita.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/FigVOnoto.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/FigVChirgua.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/FigVSaltoParu.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/FigVCerroCuevaIglesias.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/FigVVigirima.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/FigVChipaque.png") ;
				break;
			
			}	
			}	
			
			else{
			switch(ubicacionM){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/AntMCostaRica.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/AntMFrancia.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/AntMInglaterra.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/AntMIndia.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/AntMNamibia.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/AntMAustralia.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/AntMPeru.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/AntMUsa.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/AntMFrancia.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/AntMInglaterra.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/AntMIndia.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/AntMNamibia.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/AntMAustralia.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/AntMPeru.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/AntMUsa.png") ;
				break;
			
			}	
				
			
			}
		if(visib==0){
			visib=1;		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
			
		
		
		});

$("#zoom3").hover(function(){
		$("#ImgToZoom").css('height','200px');
		$("#ImgToZoom").css('width','300px');
		$("#DivImgToZoom").css('margin-left','830px');
		if(count==0)
			{
				
			switch(ubicacionV){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/SonVCerroGuarani.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/SonVSantaAnita.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/SonVOnoto.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/SonVChirgua.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/SonVSaltoParu.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/SonVCerroCuevaIglesias.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/SonVVigirima.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/SonVChipaque.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/SonVSantaAnita.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/SonVOnoto.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/SonVChirgua.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/SonVSaltoParu.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/SonVCerroCuevaIglesias.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/SonVVigirima.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/SonVChipaque.png") ;
				break;
			
			}	
			}	
			
			else{
			switch(ubicacionM){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/SonMCostaRica.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/SonMFrancia.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/SonMInglaterra.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/SonMIndia.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/SonMNamibia.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/SonMAustralia.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/SonMPeru.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/SonMUsa.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/SonMFrancia.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/SonMInglaterra.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/SonMIndia.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/SonMNamibia.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/SonMAustralia.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/SonMPeru.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/SonMUsa.png") ;
				break;
			
			}	
				
			
			}
		if(visib==0){
			visib=1;		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
			
		
		
		});

$("#zoom4").hover(function(){
		$("#ImgToZoom").css('height','200px');		
		$("#ImgToZoom").css('width','300px');
		$("#DivImgToZoom").css('margin-left','830px');
		if(count==0)
			{
				
			switch(ubicacionV){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/NombreVCerroGuarani.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/NombreVSantaAnita.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/NombreVOnoto.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/NombreVChirgua.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/NombreVSaltoParu.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/NombreVCerroCuevaIglesias.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/NombreVVigirima.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/NombreVChipaque.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/NombreVSantaAnita.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/NombreVOnoto.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/NombreVChirgua.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/NombreVSaltoParu.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/NombreVCerroCuevaIglesias.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/NombreVVigirima.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/NombreVChipaque.png") ;
				break;
			
			}	
			}	
			
			else{
			switch(ubicacionM){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/NombreMCostaRica.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/NombreMFrancia.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/NombreMInglaterra.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/NombreMIndia.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/NombreMNamibia.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/NombreMAustralia.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/NombreMPeru.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/NombreMUsa.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/NombreMFrancia.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/NombreMInglaterra.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/NombreMIndia.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/NombreMNamibia.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/NombreMAustralia.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/NombreMPeru.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/NombreMUsa.png") ;
				break;
			
			}	
				
			
			}
		if(visib==0){
			visib=1;		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
			
		
		
		});
$("#zoomarte").hover(function(){
		$("#ImgToZoom").css('height','247px');
		$("#ImgToZoom").css('width','393px');
		$("#DivImgToZoom").css('margin-left','785px');		
		if(count==0)
			{
				
			switch(ubicacionV){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/artecerroguanari.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/artesantaanita.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/arteonoto.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/artechirgua.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/artesaltoparu.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/artecerrocuevaiglesias.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/artevigirima.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/artechipaque.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/artesantaanita.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/arteonoto.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/artechirgua.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/artesaltoparu.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/artecerrocuevaiglesias.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/artevigirima.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/artechipaque.png") ;
				break;
			
			}	
			}	
			
			else{
			switch(ubicacionM){ 
				case 0: 
					$("#ImgToZoom").attr("src", "zooms/artecostarica.png") ;
				break;
				case 1: 
					$("#ImgToZoom").attr("src", "zooms/artefrancia.png") ;
				break; 
				case 2: 
					$("#ImgToZoom").attr("src", "zooms/arteinglaterra.png") ;
				break; 
				case 3: 
					$("#ImgToZoom").attr("src", "zooms/arteindia.png") ;
				break; 
				case 4: 
					$("#ImgToZoom").attr("src", "zooms/artenamibia.png") ;
				break; 
				case 5: 
					$("#ImgToZoom").attr("src", "zooms/arteaustralia.png") ;
				break; 
				case 6: 
					$("#ImgToZoom").attr("src", "zooms/arteperu.png") ;
				break; 
				case 7: 
					$("#ImgToZoom").attr("src", "zooms/arteusa.png") ;
				break; 
				case -7: 
					$("#ImgToZoom").attr("src", "zooms/artefrancia.png") ;
				break; 
				case -6: 
					$("#ImgToZoom").attr("src", "zooms/arteinglaterra.png") ;
				break; 
				case -5: 
					$("#ImgToZoom").attr("src", "zooms/arteindia.png") ;
				break; 
				case -4: 
					$("#ImgToZoom").attr("src", "zooms/artenamibia.png") ;
				break; 
				case -3: 
					$("#ImgToZoom").attr("src", "zooms/arteaustralia.png") ;
				break; 
				case -2: 
					$("#ImgToZoom").attr("src", "zooms/arteperu.png") ;
				break; 
				case -1: 
					$("#ImgToZoom").attr("src", "zooms/arteusa.png") ;
				break;
			
			}	
				
			
			}
		if(visib==0){
			visib=1;		
			$("#DivImgToZoom").css("display","block");		
			
			
			
			}
		else{
		visib=0;
			$("#DivImgToZoom").css("display","none");
			
			}
			
		
		
		});
});

