// "+N more photos" inline expand
document.addEventListener('click', function (e) {
  const btn = e.target.closest('.more-photos-btn');
  if (!btn) return;
  const spread = btn.closest('.spread');
  const extra = spread.querySelector('.extra-photos');
  if (!extra) return;
  const expanded = btn.getAttribute('aria-expanded') === 'true';
  if (expanded) {
    extra.hidden = true;
    btn.setAttribute('aria-expanded', 'false');
    const n = btn.dataset.extraCount;
    btn.innerHTML = `+ ${n} more photos &darr;`;
  } else {
    extra.hidden = false;
    btn.setAttribute('aria-expanded', 'true');
    btn.innerHTML = 'show less &uarr;';
  }
});
