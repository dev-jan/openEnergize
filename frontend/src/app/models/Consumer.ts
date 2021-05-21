export interface Consumer {
  id: number;
  name: string;
  type: string;
  image?: string;
  currentConsumptionInWatt: number;
  isControllable: boolean;
  status: string;
}
