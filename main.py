{% extends 'base.html' %}
{% block content %}
<section class="panel form-panel">
    <div class="form-intro">
        <h3>Nova solicitação de folha A4</h3>
        <p>Preencha uma vez, informe a quantidade e deixe o sistema preparado para impressão no computador.</p>
    </div>

    <form method="post" action="/nova" class="request-form">
        <div class="form-grid">
            <label>
                <span>Código</span>
                <input type="text" name="codigo" placeholder="Ex.: 34263" required>
            </label>
            <label>
                <span>Origem</span>
                <input type="text" name="origem" placeholder="Ex.: CEBRASA" required>
            </label>
            <label class="full-width">
                <span>Produto</span>
                <input type="text" name="produto" placeholder="Ex.: CORONA CERO LT 350ML" required>
            </label>
            <label>
                <span>Recebimento</span>
                <input type="date" name="recebimento" required>
            </label>
            <label>
                <span>Conferente</span>
                <input type="text" name="conferente" placeholder="Ex.: Sérgio" required>
            </label>
            <label>
                <span>Vencimento</span>
                <input type="date" name="vencimento" required>
            </label>
            <label>
                <span>Quantidade de folhas</span>
                <input type="number" name="quantidade" min="1" step="1" value="1" required>
            </label>
            <label>
                <span>Rua <small>(controle interno)</small></span>
                <input type="text" name="rua" placeholder="Ex.: Rua 07" required>
            </label>
            <label class="full-width">
                <span>Endereço <small>(controle interno)</small></span>
                <input type="text" name="endereco" placeholder="Ex.: Porta 02 / Ala Norte" required>
            </label>
            <label class="full-width">
                <span>Observação opcional</span>
                <textarea name="observacao" rows="3" placeholder="Campo interno para apoio da operação"></textarea>
            </label>
        </div>

        <div class="form-actions">
            <a href="/" class="btn btn-secondary">Cancelar</a>
            <button type="submit" class="btn btn-primary">Salvar solicitação</button>
        </div>
    </form>
</section>
{% endblock %}
