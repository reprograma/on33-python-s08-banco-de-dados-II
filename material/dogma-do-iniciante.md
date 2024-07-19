# Dogma do iniciante

Feito pela professora Daviny Letícia

1. **Nunca Delete Sem Saber o Que Está Fazendo**: Sempre use `WHERE` com `DELETE`. Se não tiver certeza, faça um `UPDATE` para marcar como removido.

2. **Backup Antes de Tudo**: Sempre faça backup antes de mexer em dados importantes. Perder dados por falta de backup é uma dor de cabeça que você pode evitar.

3. **Índices Aceleram o Processo**: Use índices nas colunas que você consulta muito. Isso torna as buscas mais rápidas e o sistema mais eficiente.

4. **Não Duplicar é Melhor**: Evite duplicar dados. Mantenha tudo organizado e evite confusões e problemas no futuro.

5. **Queries Simples São Melhores**: Escreva consultas claras e simples. Consultas complexas são difíceis de entender e manter.

6. **Use Transações Para Seguir o Fluxo**: Quando for fazer mudanças, use transações para garantir que tudo saia certo ou nada aconteça.

7. **Teste Antes de Lançar**: Sempre teste suas mudanças em um ambiente de desenvolvimento ou com dados de teste. Isso evita surpresas indesejadas.

8. **Conheça Seus Dados**: Entenda a estrutura dos dados com os quais está trabalhando. Isso ajuda a evitar erros e a trabalhar de forma mais eficiente.

9. **Documente Suas Decisões**: Anote o que você faz e por quê. Isso ajuda a lembrar o que foi feito e a explicar a outras pessoas se necessário.

10. **Mantenha a Simplicidade**: Não complique suas consultas e scripts. Simplicidade é a chave para manter tudo funcionando bem.

11. **Cuidado ao Atualizar**: Quando usar `UPDATE`, sempre adicione um `WHERE` para não atualizar todos os registros acidentalmente. Se estiver atualizando quantidades em estoque, use `quant = quant + valor` ou `quant = quant - valor` para garantir que o estoque seja ajustado corretamente.

12. **Queries Eficientes**: Evite problemas de performance criando queries diretas e evitando múltiplas consultas desnecessárias.

13. **Segurança Sempre em Mente**: Valide e sanitize todos os dados de entrada. Proteja seu sistema contra ataques e dados inválidos.

14. **Reutilize Código**: Não repita código desnecessariamente. Reutilizar funções e scripts facilita a manutenção e reduz erros.

15. **Documente Consultas Complexas**: Adicione comentários às suas consultas complicadas para facilitar a compreensão no futuro.

16. **Use Controle de Versão**: Mantenha seus scripts e procedimentos sob controle de versão. Isso ajuda a gerenciar mudanças e colaborações.

17. **Mantenha Consistência**: Use uma nomenclatura consistente e clara. Isso torna o trabalho mais organizado e fácil de entender.

18. **Monitore e Otimize**: Fique de olho na performance das suas consultas e faça ajustes quando necessário para manter tudo funcionando bem.

19. **Teste o Processo de Recuperação**: Faça backup e teste a recuperação dos dados para garantir que você pode restaurar tudo se necessário.

20. **Aprenda com os Erros**: Quando algo dá errado, documente o que aconteceu e como você resolveu. Isso ajuda a evitar cometer os mesmos erros novamente.

Esses dogmas são diretos e práticos para ajudar iniciantes a evitar erros comuns e manter tudo funcionando de maneira eficiente e segura.