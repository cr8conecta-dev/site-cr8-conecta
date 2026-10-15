
document.addEventListener('DOMContentLoaded', () => {
    // Hamburger Menu
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mainNav = document.querySelector('.main-nav');
    const navLinks = document.querySelectorAll('.nav-links a');

    if (hamburgerMenu && mainNav) {
        hamburgerMenu.addEventListener('click', () => {
            mainNav.classList.toggle('open');
        });
    }

    // Close menu when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mainNav.classList.contains('open')) {
                mainNav.classList.remove('open');
            }
        });
    });

    // Scroll reveal animations
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.scroll-reveal, .blur-in').forEach(el => {
        revealObserver.observe(el);
    });

    // Progress bar
    const progressBar = document.querySelector('.progress-bar');
    if (progressBar) {
        window.addEventListener('scroll', () => {
            const scrollTop = document.documentElement.scrollTop;
            const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrollProgress = (scrollTop / scrollHeight) * 100;
            progressBar.style.width = `${scrollProgress}%`;
        });
    }

    // Testimonial Carousel
    const testimonialSlides = document.querySelector('.testimonial-slides');
    if (testimonialSlides) {
        const slides = document.querySelectorAll('.testimonial-slide');
        const prevButton = document.querySelector('#testimonials .prev');
        const nextButton = document.querySelector('#testimonials .next');
        let currentIndex = 0;

        const showSlide = (index) => {
            const slideWidth = slides[0].clientWidth;
            testimonialSlides.style.transform = `translateX(${-index * slideWidth}px)`;
        };

        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.length - 1;
            showSlide(currentIndex);
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < slides.length - 1) ? currentIndex + 1 : 0;
            showSlide(currentIndex);
        });
         window.addEventListener('resize', () => showSlide(currentIndex));
    }

    // Niche Carousel
    const nicheSlidesWrapper = document.querySelector('.niche-slides');
    if (nicheSlidesWrapper) {
        const nicheSlides = document.querySelectorAll('.niche-slide');
        const nichePrevButton = document.querySelector('#niches .prev');
        const nicheNextButton = document.querySelector('#niches .next');
        let nicheCurrentIndex = 0;
        
        const getSlidesToShow = () => window.innerWidth <= 768 ? 1 : 3;

        const showNicheSlides = (index) => {
            const slideMargin = parseInt(window.getComputedStyle(nicheSlides[0]).marginRight) || 24; //Fallback to 24 if parsing fails
            const slideWidth = nicheSlides[0].offsetWidth + slideMargin;
            const totalSlides = nicheSlides.length;
            const slidesToShow = getSlidesToShow();
            const maxIndex = totalSlides - slidesToShow;

            if (index > maxIndex) {
                nicheCurrentIndex = maxIndex;
            }
             if (index < 0) {
                nicheCurrentIndex = 0;
            }

            nicheSlidesWrapper.style.transform = `translateX(${-nicheCurrentIndex * slideWidth}px)`;
        };

        nichePrevButton.addEventListener('click', () => {
            const slidesToShow = getSlidesToShow();
            nicheCurrentIndex -= slidesToShow;
            showNicheSlides(nicheCurrentIndex);
        });

        nicheNextButton.addEventListener('click', () => {
            const slidesToShow = getSlidesToShow();
            nicheCurrentIndex += slidesToShow;
            showNicheSlides(nicheCurrentIndex);
        });

        window.addEventListener('resize', () => {
            nicheCurrentIndex = 0; // Reset on resize
            showNicheSlides(nicheCurrentIndex)
        });
        // Initial call
        showNicheSlides(nicheCurrentIndex)
    }

    // --- FAQ Accordion --- //
    const faqContainer = document.querySelector('.faq-container');
    if (faqContainer) {

        const handleFaqClick = (e) => {
            const trigger = e.target.closest('.faq-trigger');
            if (!trigger) return;

            const item = trigger.closest('.faq-item');
            const content = item.querySelector('.faq-content');
            const contentInner = item.querySelector('.faq-content-inner');

            const isActive = item.classList.contains('active');

            // Close all other items
            faqContainer.querySelectorAll('.faq-item').forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.faq-content').style.maxHeight = '0px';
                    otherItem.querySelector('.faq-icon').textContent = '+';
                }
            });

            // Toggle the clicked item
            if (isActive) {
                item.classList.remove('active');
                content.style.maxHeight = '0px';
                trigger.querySelector('.faq-icon').textContent = '+';
            } else {
                item.classList.add('active');
                content.style.maxHeight = contentInner.scrollHeight + 'px';
                trigger.querySelector('.faq-icon').textContent = '−';
            }
        };

        const initFirstFaqItem = () => {
            const firstItem = faqContainer.querySelector('.faq-item');
            if (firstItem && firstItem.classList.contains('active')) {
                const content = firstItem.querySelector('.faq-content');
                const contentInner = firstItem.querySelector('.faq-content-inner');
                const icon = firstItem.querySelector('.faq-icon');
                content.style.maxHeight = contentInner.scrollHeight + 'px';
                icon.textContent = '−';
            }
        };

        faqContainer.addEventListener('click', handleFaqClick);
        initFirstFaqItem();
    }
});
