(function () {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");
    
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion=confirm('¿Seguro de eliminar el documento cargado?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();