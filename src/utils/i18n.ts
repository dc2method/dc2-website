export function getLocale(url: URL): 'fr' | 'en' {
  const pathname = url.pathname;
  if (pathname.startsWith('/en/') || pathname === '/en') return 'en';
  return 'fr'; // default
}

export function getLocalizedPath(path: string, locale: 'fr' | 'en'): string {
  if (locale === 'fr') return path;
  return `/en${path}`;
}

export const translations = {
  fr: {
    'nav.methodology': 'Méthodologie',
    'nav.about': 'À Propos',
    'hero.tagline': 'Développement logiciel structuré assisté par LLM',
    'hero.message': 'La méthodologie qui transforme les LLM de générateurs statistiques en outils de développement structurés, testés et maintenables.',
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

export function t(key: string, locale: 'fr' | 'en'): string {
  return translations[locale][key as keyof typeof translations['fr']] || key;
}
