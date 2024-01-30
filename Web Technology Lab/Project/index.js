/* MENU */
const headerElement = document.querySelector('.header');
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link =>
	link.addEventListener('click', () => {
		headerElement.classList.toggle('nav-open');
	})
);


/* STICKY NAVIGATION */
const heroElement = document.querySelector('.section-hero');
const navObserver = new IntersectionObserver(
	function (entries) {
		!entries[0].isIntersecting
			? document.body.classList.add('sticky')
			: document.body.classList.remove('sticky');
	},
	{
		root: null,
		threshold: 0,
	}
);

navObserver.observe(heroElement);

/* SCROLL ANIMATE */
const appShots = document.querySelectorAll('.mobile-bg');
const scrollObserver = new IntersectionObserver(entries => {
	entries.forEach(entry => {
		entry.isIntersecting
			? entry.target.classList.toggle('animate-img')
			: entry.target.classList.remove('animate-img');
	});
});

appShots.forEach(el => scrollObserver.observe(el));


/* FORM FUNCTIONALITY */
function submission(event) {
	event.preventDefault();

	const name = document.querySelector('#user-name').value;
	const planChoice = document.querySelector('#user-plan').value;
	const message = document.querySelector('.submission');

	if (planChoice) {
		message.style.display = 'block';
		message.textContent = `You have been registered successfully. Thank you for your interest in the ${planChoice} plan, ${name}.`;
	} else {
		message.style.display = 'block';
		message.textContent = `Sorry, you need to choose a plan to proceed!`;
	}
}

const subscribeForm = document.querySelector('#form-subscribe-element');
subscribeForm.addEventListener('submit', submission);
