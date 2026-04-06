export interface InstitutionMeta {
  country: string;
  flag: string;
  signatory: boolean;
}

const COUNTRY_FLAGS: Record<string, string> = {
  BE: "🇧🇪",
  DE: "🇩🇪",
  ES: "🇪🇸",
  FI: "🇫🇮",
  FR: "🇫🇷",
  IT: "🇮🇹",
  NL: "🇳🇱",
  CH: "🇨🇭",
  UK: "🇬🇧",
};

const META: Record<string, InstitutionMeta> = {
  "Admiral Group":    { country: "UK", flag: COUNTRY_FLAGS["UK"], signatory: true  },
  "Ageas":            { country: "BE", flag: COUNTRY_FLAGS["BE"], signatory: true  },
  "Allianz":          { country: "DE", flag: COUNTRY_FLAGS["DE"], signatory: true  },
  "Amundi":           { country: "FR", flag: COUNTRY_FLAGS["FR"], signatory: false },
  "ASR Nederland":    { country: "NL", flag: COUNTRY_FLAGS["NL"], signatory: false },
  "Aviva":            { country: "UK", flag: COUNTRY_FLAGS["UK"], signatory: true  },
  "AXA":              { country: "FR", flag: COUNTRY_FLAGS["FR"], signatory: false },
  "Commerzbank":      { country: "DE", flag: COUNTRY_FLAGS["DE"], signatory: true  },
  "Crédit Agricole":  { country: "FR", flag: COUNTRY_FLAGS["FR"], signatory: true  },
  "Deutsche Börse":   { country: "DE", flag: COUNTRY_FLAGS["DE"], signatory: false },
  "Eurazeo":          { country: "FR", flag: COUNTRY_FLAGS["FR"], signatory: false },
  "GBL":              { country: "BE", flag: COUNTRY_FLAGS["BE"], signatory: false },
  "ING":              { country: "NL", flag: COUNTRY_FLAGS["NL"], signatory: true  },
  "Julius Baer":      { country: "CH", flag: COUNTRY_FLAGS["CH"], signatory: true  },
  "KBC":              { country: "BE", flag: COUNTRY_FLAGS["BE"], signatory: true  },
  "Legal & General":  { country: "UK", flag: COUNTRY_FLAGS["UK"], signatory: true  },
  "NN Group":         { country: "NL", flag: COUNTRY_FLAGS["NL"], signatory: true  },
  "Nordea":           { country: "FI", flag: COUNTRY_FLAGS["FI"], signatory: true  },
  "Phoenix Group":    { country: "UK", flag: COUNTRY_FLAGS["UK"], signatory: true  },
  "Santander":        { country: "ES", flag: COUNTRY_FLAGS["ES"], signatory: true  },
  "Schroders":        { country: "UK", flag: COUNTRY_FLAGS["UK"], signatory: false },
  "Société Générale": { country: "FR", flag: COUNTRY_FLAGS["FR"], signatory: false },
  "Swiss Re":         { country: "CH", flag: COUNTRY_FLAGS["CH"], signatory: true  },
  "UniCredit":        { country: "IT", flag: COUNTRY_FLAGS["IT"], signatory: false },
  "Zurich":           { country: "CH", flag: COUNTRY_FLAGS["CH"], signatory: true  },
};

export function getMeta(company: string): InstitutionMeta {
  return META[company] ?? { country: "—", flag: "🏦", signatory: false };
}

export const MATURITY_COLORS: Record<number, string> = {
  0: "#9ca3af", // gray-400
  1: "#f87171", // red-400
  2: "#fb923c", // orange-400
  3: "#fbbf24", // amber-400
  4: "#4ade80", // green-400
};

export const MATURITY_LABELS: Record<number, string> = {
  0: "Not Started",
  1: "Initial",
  2: "Developing",
  3: "Defined",
  4: "Advanced",
};

export const MATURITY_BG: Record<number, string> = {
  0: "bg-gray-200 text-gray-700",
  1: "bg-red-100 text-red-700",
  2: "bg-amber-100 text-amber-700",
  3: "bg-yellow-100 text-yellow-700",
  4: "bg-green-100 text-green-700",
};

export const PART_COLORS: Record<string, string> = {
  "Part A": "bg-blue-600",
  "Part B": "bg-orange-500",
  "Part C": "bg-purple-600",
};

export const PART_TEXT_COLORS: Record<string, string> = {
  "Part A": "text-blue-700",
  "Part B": "text-orange-600",
  "Part C": "text-purple-700",
};

export const PART_BORDER_COLORS: Record<string, string> = {
  "Part A": "border-blue-200",
  "Part B": "border-orange-200",
  "Part C": "border-purple-200",
};

export const PART_BG_COLORS: Record<string, string> = {
  "Part A": "bg-blue-50",
  "Part B": "bg-orange-50",
  "Part C": "bg-purple-50",
};

export const PART_NAMES: Record<string, string> = {
  "Part A": "Financed Emissions",
  "Part B": "Facilitated Emissions",
  "Part C": "Insurance-Associated Emissions",
};
