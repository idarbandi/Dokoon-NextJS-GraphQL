# Dokoon-NextJS-GraphQL 🚀

**A Modern Transition from REST to GraphQL**  
🔥 *Reimagining [Dokoon-NextDRF](https://github.com/idarbandi/Dokoon-NextDRF) with GraphQL Power*  

![Tech Stack](https://img.shields.io/badge/Stack-GraphQL%20|%20Next.js%20|%20Django-informational?style=flat&logo=graphql&logoColor=white&color=e535ab)
![Authentication](https://img.shields.io/badge/Security-HTTP_Only_Cookies-success?style=flat&logo=shield-check)

## 📖 Overview
This project evolves from **[Dokoon-NextDRF](https://github.com/idarbandi/Dokoon-NextDRF)** (Next.js + Django REST Framework) to demonstrate:  
✨ **GraphQL API implementation** as a modern alternative to REST  
✨ **HTTP-Only Cookie Authentication** for enhanced security  
✨ Focused on **backend API architecture** over UI polish  

> **Note:** While the original project emphasized full-stack features, this version prioritizes **GraphQL implementation patterns** and **secure auth flows**.

## 🛠 Key Features
| **Feature**          | **Description**                                  | 
|----------------------|--------------------------------------------------|
| 📡 **GraphQL API**    | Complete replacement of DRF endpoints with GraphQL queries/mutations |
| 🔒 **Auth Strategy**  | JWT authentication via HTTP-Only cookies (No localStorage!) |
| ⚡ **Performance**    | Optimized data fetching with GraphQL's query flexibility |
| 🧩 **Modular Design** | Clean separation between Django models and GraphQL resolvers |

## 🌐 Tech Stack
**Frontend**  
![Next.js](https://img.shields.io/badge/Next.js-14.1-black?logo=next.js&logoColor=white)
![GraphQL Client](https://img.shields.io/badge/Apollo_Client-3.8-purple?logo=apollographql)

**Backend**  
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![GraphQL Server](https://img.shields.io/badge/Graphene-3.3-blueviolet?logo=graphql)

## 🚀 Installation
**1. Clone Repository**
```bash
git clone https://github.com/idarbandi/Dokoon-NextJS-GraphQL.git
cd Dokoon-NextJS-GraphQL
```

**2. Frontend Setup**  
```bash
cd frontend
npm install
npm run dev
```

**3. Backend Setup**  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py runserver
```

## 🔍 Why GraphQL Over DRF?
- **Eliminated Over-fetching**: Clients request **exact data needs**  
- **Single Endpoint**: `/graphql` replaces multiple REST endpoints  
- **Strong Typing**: Schema-first development with Graphene-Django  
- **Frontend Flexibility**: Next.js seamlessly consumes GraphQL API  

## 🤝 Contributing
PRs welcome! Please follow:
1. Create feature branch: `git checkout -b feat/your-feature`
2. Maintain consistent GraphQL schema design
3. Test auth flows with HTTP-only cookies
4. Update documentation accordingly

---

**Crafted with ❤️ by [idarbandi](https://github.com/idarbandi)**  
📫 **Contact**: [darbandidr99@gmail.com](mailto:darbandidr99@gmail.com)  
💼 **Connect**: [LinkedIn Profile](https://www.linkedin.com/in/amir-darbandi-72526b25b/)  
🐛 **Report Issues**: [GitHub Issues](https://github.com/idarbandi/Dokoon-NextJS-GraphQL/issues)
```
