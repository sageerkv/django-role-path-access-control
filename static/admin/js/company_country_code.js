document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.querySelector('.country-select');
    const phoneInput = document.querySelector('.phone-input');
    const whatsappInput = document.querySelector('.whatsapp-input');

    if (!countrySelect) return;

    // Parse country codes
    const countryCodes = JSON.parse(countrySelect.dataset.codes || '{}');

    // Wrap inputs with span
    function wrapInput(input) {
        const wrapper = document.createElement('div');
        wrapper.style.display = 'flex';
        wrapper.style.alignItems = 'center';
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);
        return wrapper;
    }

    const phoneWrapper = wrapInput(phoneInput);
    const whatsappWrapper = wrapInput(whatsappInput);

    function updateCode() {
        const selectedId = countrySelect.value;
        const code = countryCodes[selectedId] || '';

        // Remove old spans
        phoneWrapper.querySelectorAll('.country-code-span').forEach(el => el.remove());
        whatsappWrapper.querySelectorAll('.country-code-span').forEach(el => el.remove());

        if (code) {
            const phoneSpan = document.createElement('span');
            phoneSpan.className = 'country-code-span';
            phoneSpan.textContent = `${code}`;
            phoneSpan.style.marginRight = '5px';
            phoneSpan.style.fontWeight = 'bold';
            phoneWrapper.insertBefore(phoneSpan, phoneInput);

            const whatsappSpan = document.createElement('span');
            whatsappSpan.className = 'country-code-span';
            whatsappSpan.textContent = `${code}`;
            whatsappSpan.style.marginRight = '5px';
            whatsappSpan.style.fontWeight = 'bold';
            whatsappWrapper.insertBefore(whatsappSpan, whatsappInput);
        }
    }

    // Initial code display
    updateCode();

    // Listen to Select2 change event
    $(countrySelect).on('change', updateCode);
});
