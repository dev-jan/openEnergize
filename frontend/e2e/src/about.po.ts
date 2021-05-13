import { browser, by, element } from 'protractor';

export class AboutPage {
  async navigateTo(): Promise<unknown> {
    return browser.get(browser.baseUrl + '/about');
  }

  async getLicenseLinks(): Promise<string> {
    return element.all(by.css('app-about a')).getAttribute('href');
  }
}
