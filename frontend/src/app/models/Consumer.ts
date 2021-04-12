export interface Consumer {
  id: number;
  name: string;
  type: string;
  currentConsumptionInWatt: number;
  isControllable: boolean;
  status: string;
}
