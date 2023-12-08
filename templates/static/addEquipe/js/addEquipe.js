$(document).ready(function () {
    var mecanicosSelecionados = [];

    $('#add-mecanico').click(function () {
        var mecanicoId = $('#select-mecanico').val();
        var mecanicoNome = $('#select-mecanico option:selected').data('nome');

        var mecanico = {
            id: parseInt(mecanicoId),  // Certifique-se de que o ID é tratado como um número
            nome: mecanicoNome
        };

        mecanicosSelecionados.push(mecanico);
        updateMecanicosSelecionados();
    });

    function updateMecanicosSelecionados() {
        var container = $('#mecanicos-selecionados-container');
        container.empty();

        mecanicosSelecionados.forEach(function (mecanico) {
            var linha = $('<div>').text(mecanico.nome);
            container.append(linha);
        });

        // Crie uma lista simples de IDs, não uma string JSON
        var mecanicosIds = mecanicosSelecionados.map(mecanico => mecanico.id);
        $('#mecanicos-selecionados').val(mecanicosIds.join(','));  // Unir IDs em uma string com vírgulas
    }
});