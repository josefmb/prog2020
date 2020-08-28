$(function () {
    $("#list").click(function(){
        $.ajax({
            url: "http://localhost:5000/listar_times",
            method: "GET",
            dataType: "json",
            success: listTimes,
            error: function () {
                alert("Erro");
            }
        });
    });

    function listTimes(lista_time) {
        for (time of lista_time) {
            linha_atual = `<tr> 
                        <td>${time.id}</td> 
                        <td>${time.nome}</td> 
                        <td>${time.esporte}</td> 
                      </tr>`;

            $('#tableTimeBody').append(linha_atual);
        }
    }

    $("#btnInclude").click(function(){
        // obtendo os dados da tela
        nameTime = $("#nameTime").val();
        nameSport = $("#nameSport").val();
        // preparar os dados para envio(json)
        var dados = JSON.stringify({nome: nameTime, esporte: nameSport});
        // enviar para o Beck-end
        $.ajax({
            url: 'http://localhost:5000/incluir_times',
            type: 'POST',
            contentType: 'application/json', //enviando os dados em json
            dataType: 'json',
            data: dados,
            success: incluirTime,
            error: erroIncluirTime
        });
        function incluirTime(resposta) {
            if (resposta.resultado == "ok") {
                //exibe mensagem de sucesso
                alert("Time incluído com sucesso");
                $("#nameTime").val("");
                $("#nameSport").val("");
            } else {
                alert("Erro no incluir");
            }
        }
        function erroIncluirTime(resposta) {
            alert("Não deu certo pra incluir no backend");
        }
    });
});