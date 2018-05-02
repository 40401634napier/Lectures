$(function(){
	$.ajax({
		url:'/api/info',
		success:function(data){
			console.log('get info');
			$('#info').html(JSON.stringify(data,null,''));
			$('#description').html(data['description']);
				
		}
	});
	$('#calc').click(function(){
		$('#info').css('display',"none");
		$('#description').css('display',"none");

		$.ajax({
			url:'/api/calc?a='+document.getElementById('a').value+'&b='+
			document.getElementById('b').value,
		  success:function(data){
		  	$('#add').html(data['a']+'+'+data['b']+
		  		'='+ data['add']);
		  	$('#substract').html(data['a']+'-'+data['b']+
		  		'='+ data['substract']);
		  	$('#multiply').html(data['a']+'*'+data['b']+
		  		'='+ data['multiply']);
		  	$('#divide').html(data['a']+'/'+data['b']+
		  		'='+ data['divide']);
		  }
		})
	})
})