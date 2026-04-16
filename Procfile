{% extends 'base.html' %}
{% block content %}
<section class="panel detail-header">
    <div>
        <span class="chip">Rua {{ rua }}</span>
        <h3>{{ endereco }}</h3>
        <p>Controle por agrupamento para não perder a sequência depois da impressão.</p>
    </div>

    <div class="action-row">
        <a class="btn btn-secondary" href="/">Voltar</a>
        <a class="btn btn-primary" href="/imprimir?ids={% for item in items %}{{ item['id'] }}{% if not loop.last %},{% endif %}{% endfor %}" target="_blank">Imprimir grupo</a>
    </div>
</section>

<section class="panel table-panel">
    <div class="table-wrap">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Status</th>
                    <th>Código</th>
                    <th>Produto</th>
                    <th>Origem</th>
                    <th>Receb.</th>
                    <th>Venc.</th>
                    <th>Conferente</th>
                    <th>Qtd.</th>
                    <th>Criado em</th>
                    <th>Ação</th>
                </tr>
            </thead>
            <tbody>
                {% for item in items %}
                <tr>
                    <td>#{{ item['id'] }}</td>
                    <td><span class="badge {{ item['status']|lower }}">{{ item['status'] }}</span></td>
                    <td>{{ item['codigo'] }}</td>
                    <td>{{ item['produto'] }}</td>
                    <td>{{ item['origem'] }}</td>
                    <td>{{ item['recebimento'] }}</td>
                    <td>{{ item['vencimento'] }}</td>
                    <td>{{ item['conferente'] }}</td>
                    <td>{{ item['quantidade'] }}</td>
                    <td>{{ item['created_at']|br_datetime }}</td>
                    <td>
                        {% if item['status'] == 'IMPRESSO' %}
                        <form method="post" action="/reabrir/{{ item['id'] }}">
                            <button class="btn btn-ghost" type="submit">Reabrir</button>
                        </form>
                        {% else %}
                        <span class="muted">Pendente</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</section>
{% endblock %}
