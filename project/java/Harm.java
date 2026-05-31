package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A negative impact that may be experienced by individuals,
groups, communities, organizations, society, the environment, or
the planet (Figure 1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Harm extends NamedThingRMF {

  private String harmCategory;
  private String harmToPeopleSubcategory;
  private String magnitude;
  private List<NamedThingRMF> affects;


}