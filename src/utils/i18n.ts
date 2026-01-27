export function getLocale(url: URL): 'en' | 'fr' {
  const pathname = url.pathname;
  if (pathname.startsWith('/fr/') || pathname === '/fr') return 'fr';
  return 'en'; // default (English now)
}

export function getLocalizedPath(path: string, locale: 'en' | 'fr'): string {
  if (locale === 'en') return path;
  return `/fr${path}`;
}

export const translations = {
  fr: {
    'nav.methodology': 'Méthodologie',
    'nav.about': 'À Propos',
    'hero.tagline': 'Développement logiciel structuré assisté par LLM',
    'hero.message': 'La méthodologie pour intégrer et gouverner des composants IA non-déterministes dans vos systèmes critiques.',
    'hero.cta.primary': 'Découvrir la Méthodologie →',
    'hero.cta.secondary': 'Voir les 6 Phases',
    'footer.methodology': 'Méthodologie',
    'footer.resources': 'Ressources',
    'footer.about': 'À Propos',
    'footer.license': 'Licence CC BY-SA 4.0',
    'footer.created-by': 'Créé par',
  },
  en: {
    'nav.methodology': 'Methodology',
    'nav.about': 'About',
    'hero.tagline': 'Structured LLM Development',
    'hero.message': 'The methodology that transforms LLMs from statistical generators into structured, tested, and maintainable development tools.',
    'hero.cta.primary': 'Discover the Methodology →',
    'hero.cta.secondary': 'See the 6 Phases',
    'footer.methodology': 'Methodology',
    'footer.resources': 'Resources',
    'footer.about': 'About',
    'footer.license': 'License CC BY-SA 4.0',
    'footer.created-by': 'Created by',
  },
};

export function t(key: string, locale: 'en' | 'fr'): string {
  return translations[locale][key as keyof typeof translations['fr']] || key;
}
