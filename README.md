# KAYTIM Dosya Merkezi

Site: https://kaytim.neocities.org/

## GitHub Secret
Repository secrets içine:
`KAYTIM_NEOCITIES_API_KEY`

## Kurulum
1. Bu klasörün içeriğini `d20k38/imran` repository'sine ekleyin.
2. `.github/workflows/update-kaytim-files.yml` workflow'unu GitHub'a yükleyin.
3. İlk kez Actions > KAYTIM Neocities Dosya Listesini Güncelle > Run workflow ile çalıştırın.
4. `index.html` dosyasını KAYTIM Neocities'e yükleyin.
5. Mevcut cron-job.org GitHub tokenı Actions: Write yetkisine sahipse, yeni workflow için URL:
`https://api.github.com/repos/d20k38/imran/actions/workflows/update-kaytim-files.yml/dispatches`
Body:
`{"ref":"main"}`

Headers:
Accept: application/vnd.github+json
Authorization: Bearer GITHUB_TOKEN
X-GitHub-Api-Version: 2026-03-10
Content-Type: application/json

Not: Gerçek tokenı paylaşmayın.
