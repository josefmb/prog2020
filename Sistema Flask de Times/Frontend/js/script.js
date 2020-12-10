$(function () {
    mostrarConteudo("home");

    $("#home").click(function(){
        mostrarConteudo("home")
    });

    $("#listarTimes").click(function(){
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
        $("#tableTimeBody").empty();

        mostrarConteudo("times");

        for (time of lista_time) {
            linha_atual = `<tr>
                        <td>${time.id}</td>
                        <td>${time.nome}</td>
                        <td>${time.esporte}</td>
                        <td><a href=# id="${time.id}" class="excluirTime">
                            <p class="badge badge-danger">Excluir</p> </a> </td>
                      </tr>`;

            $('#tableTimeBody').append(linha_atual);
        }
    }

    $("#listarTecnicos").click(function(){
        $.ajax({
            url: "http://localhost:5000/listar_tecnicos",
            method: "GET",
            dataType: "json",
            success: listTecnicos,
            error: function () {
                alert("Erro");
            }
        });
    });

    function listTecnicos(lista_tecnicos) {
        $("#tableTecnicoBody").empty();

        mostrarConteudo("tecnicos");

        for (tecnico of lista_tecnicos) {
            linha_atual = `<tr>
                        <td>${tecnico.id}</td>
                        <td>${tecnico.nome}</td>
                        </tr>`;

            $('#tableTecnicoBody').append(linha_atual);
        }
    }

    $("#listarInstituicoes").click(function(){
        $.ajax({
            url: "http://localhost:5000/listar_instituicoes",
            method: "GET",
            dataType: "json",
            success: listInstituicoes,
            error: function () {
                alert("Erro");
            }
        });
    });

    function listInstituicoes(lista_instituicoes) {
        $("#tableInstituicaoBody").empty();

        mostrarConteudo("instituicoes");

        for (instituicao of lista_instituicoes) {
            linha_atual = `<tr>
                        <td>${instituicao.id}</td>
                        <td>${instituicao.nome}</td>
                        <td>${instituicao.time.nome}</td>
                        <td>${instituicao.time.esporte}</td>
                        <td>${instituicao.tecnico.nome}</td>
                        </tr>`;

            $('#tableInstituicaoBody').append(linha_atual);
        }
    }

    function mostrarConteudo(conteudo){
        $("#times").addClass('d-none');
        $("#tecnicos").addClass('d-none');
        $("#instituicoes").addClass('d-none');
        $(`#${conteudo}`).removeClass('d-none');
    }

    $("#btnInclude").click(function(){
        // obtendo os dados da tela
        nameTime = $("#nameTime").val();
        nameSport = $("#nameSport").val();
        // preparar os dados para envio(json)
        let dados = JSON.stringify({nome: nameTime, esporte: nameSport});
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

    $(document).on("click", ".excluirTime", function() {
        let IdTime = $(this).attr("id");

        $.ajax({
          url: `http://localhost:5000/excluir_time/${IdTime}`,
          type: "DELETE",
          dataType: 'json',
          success: excluirTime,
          error: erroExcluirTime
        });

        function excluirTime(retorno) {
          if (retorno.resultado === "ok") {
            $(`#linha_${IdTime}`).fadeOut(1000, () => {
                alert("Time excluído com êxito!")
            });
          } else {
            alert(`Algo deu errado: ${retorno.resultado}: ${retorno.detalhes}`);
          }
        };
        function erroExcluirTime(retorno) {
            alert("Não deu certo para excluir o Time");
        }
    });
});