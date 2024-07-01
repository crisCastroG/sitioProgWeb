var Fn = {
	// Valida el rut con su cadena completa "XXXXXXXX-X"
	validaRut : function (rutCompleto) {
		if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
			return false;
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		return (Fn.dv(rut) == digv );
	},
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}

// Uso de la función

function validarRut()
{
    let rut = document.getElementById("rut").value;
    if(!Fn.validaRut(rut))
    {
		console.log("rut invalido")
        document.getElementById("ruterror").innerHTML = "Rut inválido, ingrese su rut sin puntos y con guión.";
    }
	else
	{
		document.getElementById("ruterror").innerHTML = " ";
	}
}

function compararPass()
{
	let pass1 = document.getElementById("contraseña").value;
	let pass2 = document.getElementById("contraseña2").value;

	if(pass1 != pass2)
	{
		document.getElementById("passerror").innerHTML = "Las contraseñas no coinciden";
	}
	else
	{
		document.getElementById("passerror").innerHTML = " ";
	}
}

function getCantidad()
{
	return document.getElementById('cantidad').value
}
