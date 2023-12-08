$(document).ready(function () {
    var pecasSelecionadas = [];

    $('#add-peca').click(function () {
        var pecaId = $('#select-peca').val();
        var pecaNome = $('#select-peca option:selected').data('nome');
        var pecaPreco = parseFloat($('#select-peca option:selected').data('preco'));
        var quantidade = parseInt($('#quantidade-peca').val());

        var peca = {
            id: pecaId,
            nome: pecaNome,
            preco: pecaPreco,
            quantidade: quantidade
        };

        console.log(peca)

        pecasSelecionadas.push(peca);
        updatePecasSelecionadas();
    });

    function updatePecasSelecionadas() {
        var precoTotal = 0;

        pecasSelecionadas.forEach(function (peca) {
            precoTotal += parseFloat(peca.preco) * peca.quantidade;
        });

        console.log("Preço Total Atualizado:", precoTotal);

        $('#preco_total').val(precoTotal.toFixed(2));

        $('#preco-total-display').text("Preço Total: R$ " + precoTotal.toFixed(2));

        var pecasJSON = JSON.stringify(pecasSelecionadas.map(({ id, quantidade }) => ({ id: id, quantidade: quantidade })));
        console.log("JSON de Peças:", pecasJSON);
        $('#pecas-selecionadas').val(pecasJSON);
    }
});
