// @ts-strict-ignore
import useLocalStorage from "@dashboard/hooks/useLocalStorage";
import { createContext, ReactNode, useEffect, useRef, useState } from "react";
import { IntlProvider, ReactIntlErrorCode } from "react-intl";

export enum Locale {
  EN = "en",
  ZH_HANS = "zh-Hans",
  BI = "bi",
}

interface StructuredMessage {
  context?: string;
  string: string;
}
type LocaleMessages = Record<string, StructuredMessage>;

export const localeNames: Record<Locale, string> = {
  [Locale.EN]: "English",
  [Locale.ZH_HANS]: "简体中文",
  [Locale.BI]: "中英双语",
};

const dotSeparator = "_dot_";
const sepRegExp = new RegExp(dotSeparator, "g");

function getKeyValueJson(messages: LocaleMessages): Record<string, string> {
  if (messages) {
    const keyValueMessages: Record<string, string> = {};

    return Object.entries(messages).reduce((acc, [id, msg]) => {
      acc[id.replace(sepRegExp, ".")] = msg.string;

      return acc;
    }, keyValueMessages);
  }
}

const localeCode = process.env.LOCALE_CODE || "EN";
const defaultLocale = Locale[localeCode];

interface LocaleContextType {
  locale: Locale;
  setLocale: (locale: Locale) => void;
}
export const LocaleContext = createContext<LocaleContextType>({
  locale: defaultLocale,
  setLocale: () => undefined,
});

const { Consumer: LocaleConsumer, Provider: RawLocaleProvider } = LocaleContext;
const LocaleProvider = ({ children }: { children: ReactNode }) => {
  const [locale, setLocale] = useLocalStorage("locale", defaultLocale);
  const [messages, setMessages] = useState(undefined);
  const loaded = useRef(false);

  useEffect(() => {
    async function changeLocale() {
      if (locale !== Locale.EN && !loaded.current) {
        // It seems like Webpack is unable to use aliases for lazy imports
        const mod = await import(`../../../locale/${locale}.json`);

        setMessages(mod.default);

        if (!loaded.current) {
          loaded.current = true;
        }
      } else {
        setMessages(undefined);
      }
    }

    changeLocale();
  }, [locale]);

  return (
    <IntlProvider
      defaultLocale={defaultLocale}
      locale={locale}
      messages={getKeyValueJson(messages)}
      onError={err => {
        if (!(err.code === ReactIntlErrorCode.MISSING_TRANSLATION)) {
          console.error(err);
        }
      }}
      key={locale}
    >
      <RawLocaleProvider
        value={{
          locale,
          setLocale,
        }}
      >
        {children}
      </RawLocaleProvider>
    </IntlProvider>
  );
};

export { LocaleConsumer, LocaleProvider, RawLocaleProvider };
