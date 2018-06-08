// SECCION DEL SELECT DE PROYECTO Y ESTUDIO
estudio = $("#articulos");
estudio_val = (estudio.val()).trim();
proyecto_get = document.getElementById("proyecto");
proyecto = $("#proyecto");
// Si está seleccionado un articulos (solo pasa cuando esta en la vista editar). Muestra el proyecto al que pertenece
if (estudio_val){
    $.ajax({
        data: {},
        url: origin+'/api-gestion/estudios/'+estudio_val+"/",
        type: 'get',
        success: function (data) {
            for(var i=1;i<proyecto_get.length;i++) {
                if(proyecto_get.options[i].value == data.proyecto) {
                    proyecto_get.selectedIndex=i;
                }
            }

        }
    });
    // Apenas esté listo todo, liste solo los estudios relaciones con el proyecto
    $(document).ready(function () {
        window.setTimeout(function(){
            listarEstudios();
        },1000);
    });
}else{
    // si entra aqui es porque está en la vista de nuevo
    estudio.html("");
    estudio.append('<option value="">- Seleccione un proyecto -</option>');
}

// Mostrar los estudios en el select (solo los que pertenecen al proyecto al que pertenece)
listarEstudios = function () {
    proyecto_val = proyecto.val();
    $.ajax({
        data: {},
        url: origin+'/api-gestion/estudios/?proyecto='+proyecto_val,
        type: 'get',
        success: function (data) {
            estudio.html(""); //Limpiamos el select
            $.each(data, function(key, registro) {
                if(registro.id == estudio_val){
                    estudio.append('<option selected value='+registro.id+'>'+registro.nombre+'</option>');
                }else{
                    estudio.append('<option value='+registro.id+'>'+registro.nombre+'</option>');
                }
            });
            estudio.selectpicker('refresh'); // Refrescamos el select
        }
    });
};

// si seleccionan un proyecto, se actuliza los estudios que pertenecen a este
proyecto.change(function () {
    listarEstudios();
});