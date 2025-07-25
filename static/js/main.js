
/**
 * Esconde o elemento .mouse quando o usuário rolar o elemento com .scroll-hint.
 * Mostra novamente se voltar ao topo.
 */

document.addEventListener('DOMContentLoaded', function () {
  // Adiciona o listener de clique nos elementos timeline-box

  setTimeout(function () {
    document.querySelectorAll('.timeline-box').forEach(function (timelineBox) {

      timelineBox.addEventListener('click', function () {
        // Aguarda o modal abrir e o conteúdo ser carregado (caso seja dinâmico)

        setTimeout(() => {

          document.querySelectorAll('.scroll-hint').forEach(function (el) {

            // Exibe ou esconde o .mouse baseado no overflow
            const mouse = el.querySelector('.mouse');
            if (mouse) {
              // Verifica se há scroll possível
              const hasScroll = el.scrollHeight > el.clientHeight;
              mouse.style.opacity = hasScroll ? 1 : 0;
            }

            // Adiciona o listener de scroll apenas após o clique
            el.addEventListener('scroll', function () {
              const mouse = el.querySelector('.mouse');
              if (!mouse) return;

              if (el.scrollTop > 0) {
                mouse.style.opacity = 0;
              } else {
                mouse.style.opacity = 1;
              }
            });
          });

        }, 500);
      });

    });

  }, 1000); // Ajuste o tempo se necessário para garantir que o conteúdo foi renderizado
});


/**
 * Aplica o tema salvo no localStorage ao carregar a página
 */
document.addEventListener('DOMContentLoaded', function () {
  // Aplica o tema salvo (ou 'light' por padrão)
  const theme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', theme);

  // Adiciona listener para todos os theme-controller
  document.querySelectorAll('.theme-controller').forEach(function (el) {
    el.checked = (theme === 'dark');
    el.addEventListener('change', function () {
      // Se for checkbox, alterna entre 'dark' e 'light'
      const newTheme = el.checked ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  });
});